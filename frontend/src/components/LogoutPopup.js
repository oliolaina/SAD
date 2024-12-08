import React from "react";

function LogoutPopup() {
  const handleLogout = () => {
    if (window.confirm("Вы действительно хотите выйти?")) {
      window.location.href = "/";
    }
  };

  return (
    <div>
      <button onClick={handleLogout}>Выйти</button>
    </div>
  );
}

export default LogoutPopup;
