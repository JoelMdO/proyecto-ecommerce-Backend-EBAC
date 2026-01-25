from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import OrderManagerModel
from .serializers import OrderManagerSerializer
from address.serializers import AddressSerializer
from cart.models import CartModel
from product.models import ProductModel
from rest_framework.permissions import IsAuthenticated
#import logging
from decimal import Decimal, InvalidOperation

class OrdersAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    def get(self, request: Request):
        try:
            order = OrderManagerModel.objects.filter(user_name=request.user.get_username())
            serializer = OrderManagerSerializer(order, many=True, context={"request": request})  # type: ignore
            return Response(serializer.data)  # type: ignore
        except Exception as e:
            #logging.exception("Error in OrdersAPIView.get")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request: Request):
        try:
            data = request.data.copy()
            # Accept frontend cart list (list of product dicts). Create a CartModel server-side
            cart_val = data.get("cart")
            #logging.info("Original 'cart' value from request: %r (type=%s)", cart_val, type(cart_val)) # type: ignore
            if isinstance(cart_val, list):
                try:
                    new_cart = CartModel.objects.create()
                    for item in cart_val: # type: ignore
                        prod_id = None
                        if isinstance(item, dict):
                            prod_id = item.get("id") # type: ignore
                        elif isinstance(item, (int, str)):
                            try:
                                prod_id = int(item)
                            except Exception:
                                prod_id = None
                        if prod_id is None:
                            continue
                        try:
                            prod = ProductModel.objects.get(pk=int(prod_id)) # type: ignore
                            new_cart.products.add(prod) # type: ignore
                            #logging.info("Added product to cart: id=%s name=%s", prod.pk, getattr(prod, 'name', None))
                        except ProductModel.DoesNotExist:
                            #logging.error("Product not found for id: %s", prod_id) # type: ignore
                            return Response({"cart_error": f"Product {prod_id} not found"}, status=status.HTTP_400_BAD_REQUEST) # type: ignore
                    # Log final cart contents
                    #try:
                        cnt = new_cart.products.count() # type: ignore
                        #logging.info("New Cart %s has %d products", new_cart.pk, cnt)
                    #except Exception:
                        #logging.info("New Cart %s created (unable to count products)", new_cart.pk)
                    data["cart"] = new_cart.pk
                except Exception:
                    #logging.exception("Error creating CartModel from frontend cart")
                    return Response({"error": "Unable to create cart"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            #logging.info("DATA RECEIVED IN ORDERSAPI VIEW: %s", data)
            # If the client included nested address data, validate and create it first
            address_data = data.pop("address", None)
            if address_data:
                # address_data can be a JSON string when sent in multipart; try to parse
                if isinstance(address_data, str):
                    try:
                        import json
                        address_data = json.loads(address_data)
                    except Exception:
                        # leave as-is; AddressSerializer will handle types/validation
                        pass

                if isinstance(address_data, dict) and "user_name" not in address_data:
                    address_data["user_name"] = request.user.get_username()

                addr_serializer = AddressSerializer(data=address_data, context={"request": request})
                if not addr_serializer.is_valid():
                    #logging.error("Address validation errors: %s", addr_serializer.errors) # type: ignore
                    return Response({"address_errors": addr_serializer.errors}, status=status.HTTP_400_BAD_REQUEST) # type: ignore
                addr_serializer.save()

            # Ensure order user_name is set to the authenticated user if not provided
            if "user_name" not in data:
                data["user_name"] = request.user.get_username()

            # Normalize total: accept strings with commas or numbers
            if "total" in data:
                t = data.get("total")
                if isinstance(t, str):
                    try:
                        t_norm = t.replace(",", "")
                        data["total"] = Decimal(t_norm)
                    except (InvalidOperation, Exception):
                        # leave as-is; serializer will handle validation
                        pass
            # Defensive logging immediately before serialization to debug 400
            try:
                #logging.info("Request content type: %s", getattr(request, 'content_type', request.META.get('CONTENT_TYPE')))
                pass
            except Exception:
                #logging.info("Request content type: (unavailable)")
                pass
            #logging.info("Pre-serializer data keys: %s", list(data.keys()))
            #logging.info("Pre-serializer 'cart': %r (type=%s)", data.get('cart'), type(data.get('cart'))) # type: ignore
            #logging.info("Pre-serializer 'total': %r (type=%s)", data.get('total'), type(data.get('total'))) # type: ignore
            serializer = OrderManagerSerializer(data=data, context={"request": request})
            if serializer.is_valid():
                instance = serializer.save() # type: ignore
                # Include created cart product ids in the response for verification
                try:
                    cart_obj = instance.cart # type: ignore
                    product_ids = list(cart_obj.products.values_list('id', flat=True)) # type: ignore
                except Exception:
                    product_ids = None
                resp = serializer.data # type: ignore
                resp["cart_products"] = product_ids
                return Response(resp, status=status.HTTP_201_CREATED)  # type: ignore
            #logging.error("Order validation errors: %s", serializer.errors) # type: ignore
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # type: ignore
        except Exception as e:
            #logging.exception("Error in OrdersAPIView.post")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)