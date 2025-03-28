from ...db.session import get_supabase
class UserCRUD:
    @staticmethod
    def select_all():
        supabase = get_supabase()
        response = supabase.table("products").select("*").execute()
        return response.data

    @staticmethod
    def select_promo_products():
        supabase = get_supabase()
        response = supabase.table("products").select("*").eq("is_promo", 'TRUE').execute()
        return response.data

    @staticmethod
    def select_by_name(name):
        supabase = get_supabase()
        response = supabase.table("products").select("*").ilike("name", name).execute()
        return response.data
