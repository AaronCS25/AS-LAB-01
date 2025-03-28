from ...db.session import get_supabase

class UserCRUD:
    @staticmethod
    def select_all():
        supabase = get_supabase()
        response = supabase.table("stores").select("*").execute()
        return response.data

    @staticmethod
    def add_store(store: Store):
        supabase = get_supabase()
        response = supabase.table("stores").insert({
            "address": store.address
        }).execute()
        
        return response.data

