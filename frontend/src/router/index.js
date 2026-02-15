import { createRouter, createWebHistory } from "vue-router";
import PublicSalon from "../views/PublicSalon.vue";
import Confirm from "../views/Confirm.vue";
import Dashboard from "../views/Dashboard.vue";
import { useBookingStore } from "../stores/booking";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";

const routes = [
  { path: "/", redirect: "/login" }, // MVP : salon par défaut
  { path: "/register", component: Register },
  { path: "/login", component: Login },
  { path: "/salon/:id", component: PublicSalon },
  { path: "/confirm", component: Confirm },
  {
  path: "/dashboard",
  component: Dashboard,
  beforeEnter: (to, from, next) => {
    const token = localStorage.getItem("token");
    if (token) next();
    else next("/login");
  },
}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
