import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../axiosConfig";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        console.log("Отправляемые данные:", { username, password });
        const response = await axios.post("/login", { username, password });
        console.log("Ответ сервера:", response.data);
        if (response.data.access_token) {
            localStorage.setItem("token", response.data.access_token);
            localStorage.setItem("username", username);
            navigate("/dashboard");
        }
        else {
          console.log("not response.data.access_token");
        }
    } catch (error) {
        console.error("Ошибка:", error.message || response.data.access_token);
        setError("Неверный логин или пароль");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Вход</h1>
      <input
        type="text"
        placeholder="Логин"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Пароль"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      {error && <p>{error}</p>}
      <button type="submit">Войти</button>
      <button onClick={() => navigate("/register")}>Регистрация</button>
    </form>
  );
}

export default Login;
