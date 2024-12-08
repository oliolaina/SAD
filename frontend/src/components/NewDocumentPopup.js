import React, { useState } from "react";
import axios from "../axiosConfig";

function NewDocumentPopup() {
  const [recipient, setRecipient] = useState("");
  const [title, setTitle] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post("/documents", {
        receiver: recipient,
        title: title,
      });
      alert("Документ отправлен");
    } catch {
      setError("Ошибка отправки документа");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Новый документ</h2>
      <input
        type="text"
        placeholder="Логин получателя"
        value={recipient}
        onChange={(e) => setRecipient(e.target.value)}
      />
      <input
        type="text"
        placeholder="Название документа"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      {error && <p>{error}</p>}
      <button type="submit">Отправить</button>
    </form>
  );
}

export default NewDocumentPopup;
