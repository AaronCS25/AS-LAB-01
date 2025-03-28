from ...db.session import get_supabase

class UserCRUD:
    @staticmethod
    def add_product(product: Product):
        supabase = get_supabase()
        response = supabase.table("products").insert({
            "name": product.name,
            "price": product.price,
            "quantity": product.quantity,
            "is_promo": product.is_promo
        }).execute()
        return response.data

    @staticmethod
    def update_product(int: id, quantity: int):
        supabase = get_supabase()
        # Get the current value
        response = supabase.table("products").select("quantity").eq("id", product_id).execute()
        curr = response.data[0]['quantity']
        
        # Update 
        temp = curr + quantity
        response = supabase.table("products").update({
            "quantity": temp
        }).eq("id", product_id).execute()

        return response.data

    @staticmethod
    def substract_product(id: int, quantity: int):
        # Get the current value
        response = supabase.table("products").select("quantity").eq("id", product_id).execute()
        curr = response.data[0]['quantity']
        
        # Update 
        temp = curr - quantity
        if (temp < 0):
            return {"message": "Not enough stock"}
        else: 
            response = supabase.table("products").update({
                "quantity": temp
            }).eq("id", product_id).execute()
            return response.data
