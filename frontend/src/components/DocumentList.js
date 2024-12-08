import React, { useEffect, useState } from "react";
import axios from "axios";

function DocumentList({ type }) {
  const [documents, setDocuments] = useState([]);

  useEffect(() => {
    const fetchDocuments = async () => { // Убираем параметр `type` из этой функции
        const token = localStorage.getItem("token");
        try {
            console.log("Отправляем запрос с параметром type:", type);
            const response = await axios.get("/documents", {
                params: { type }, // Используем `type` из props
                headers: { Authorization: `Bearer ${token}` },
            });
            console.log("Ответ сервера:", response.data);
            setDocuments(response.data);
        } catch (error) {
            console.error("Ошибка получения документов:", error.response?.data || error.message);
        }
    };

    fetchDocuments(); // Вызываем функцию без параметров
}, [type]); // Добавляем `type` как зависимость


  return (
    <div>
      <h2>{type === "incoming" ? "Входящие" : "Исходящие"} документы</h2>
      <ul>
        {documents.map((doc, index) => (
          <li key={index}>{doc.title}</li>
        ))}
      </ul>
    </div>
  );
}

export default DocumentList;
