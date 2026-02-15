import { defineStore } from "pinia";
import http from "../api/http";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    user: null,
  }),
  actions: {
    async register(phone_number, fullname, password) {
      await http.post("auth/register/", { phone_number, fullname, password });
    },
    async login(phone_number, password) {
      const res = await http.post("auth/login/", { phone_number, password });
      this.token = res.data.access;
      localStorage.setItem("token", this.token);
    },
    logout() {
       try {
        http.post("auth/logout/", { refresh: this.refresh });
      } catch (err) {
        console.error("Erreur logout backend", err);
      }
    },
  },
});
