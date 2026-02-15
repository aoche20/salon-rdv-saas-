import axios from "axios";

const http = axios.create({
  baseURL: "http://127.0.0.1:8000/api/",
  timeout: 10000,
});
// Intercepteur pour ajouter le JWT à chaque requête
http.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("token");
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);
export default http;
