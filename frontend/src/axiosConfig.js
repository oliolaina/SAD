import axios from "axios";

const API_URL = "https://localhost/api";


axios.defaults.baseURL = API_URL;
axios.interceptors.request.use((config) => {
    const token = localStorage.getItem("token");
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default axios;
