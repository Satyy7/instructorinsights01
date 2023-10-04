import React from "react";
import "./Filter.css";
function Filter() {
  return (
    <>
      <div className="filter-container">
        <div className="search-box-container">
          <h4>Department</h4>
          <form>
            <input
              className="input"
              type="text"
              placeholder="Full department name..."
            />
          </form>
        </div>
        <div className="search-box-container">
          <h4>Rating</h4>
          <form>
            <input
              className="input"
              type="text"
              placeholder="EX: 5, >3.5, 2, etc..."
            />
          </form>
        </div>
        <div className="search-box-container">
          <h4>Rating Count</h4>
          <form>
            <input
              className="input"
              type="text"
              placeholder="EX: >100, =10, >=90, etc..."
            />
          </form>
        </div>
        <div className="search-box-container">
          <h4>WTA%</h4>
          <form>
            <input
              className="input"
              type="text"
              placeholder="Ex: >90, <=10, etc..."
            />
          </form>
        </div>
        <button className="filter-button">Query</button>
      </div>
    </>
  );
}

export default Filter;
