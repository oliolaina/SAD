import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "../axiosConfig";



function Register({ setUser }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/register", { username, password });
      setUser(username); // Сохраняем имя пользователя
      navigate("/dashboard");
    } catch {
      alert("Ошибка регистрации");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h1>Регистрация</h1>
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
      <button type="submit">Зарегистрироваться</button>
    </form>
  );
}

export default Register;
