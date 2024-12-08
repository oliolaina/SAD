import React, { useState, useEffect } from "react";
import DocumentList from "./DocumentList";
import NewDocumentPopup from "./NewDocumentPopup";
import LogoutPopup from "./LogoutPopup";

function Dashboard() {
  const [view, setView] = useState("incoming");
  const [user, setUser] = useState("");
  console.log(localStorage.getItem("token"));

  useEffect(() => {
    const username = localStorage.getItem("username");
    setUser(username || "Гость");
  }, []);

  return (
    <div>
      
      <div class = "main-menu">
      <aside>
        <button onClick={() => setView("incoming")}>Входящие</button>
        <button onClick={() => setView("outgoing")}>Исходящие</button>
        <button onClick={() => setView("newDocument")}>Новый документ</button>
        <button onClick={() => setView("logout")}>Выход</button>
      </aside>
      <main>
      <header>
        <h1>Добро пожаловать, {user}!</h1>
      </header>
        {view === "incoming" && <DocumentList type="incoming" />}
        {view === "outgoing" && <DocumentList type="outgoing" />}
        {view === "newDocument" && <NewDocumentPopup />}
        {view === "logout" && <LogoutPopup />}
      </main>
      </div>
    </div>
  );
}

export default Dashboard;
