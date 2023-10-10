import React from "react";
import "./header.css";
import { useState, useEffect } from "react";

function Header() {
  const [darkMode, setDarkMode] = useState(false);
  useEffect(() => {
    document.body.classList.toggle("dark-mode", darkMode);
  }, [darkMode]);

  return (
    <div className="header">
      <h4 className="title">Instructor Insights</h4>
      <button className="night-button" onClick={() => setDarkMode(!darkMode)}>
        {darkMode ? "Light" : "Dark"}
      </button>
    </div>
  );
}

export default Header;
