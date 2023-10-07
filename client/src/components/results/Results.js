import React from "react";
import "./Results.css";
function Results({ data }) {
  return (
    <>
      <div className="results-container"></div>
      <div className="results-header">Results</div>
      <div className="results-body">
        <div>
          {data.map((prof, index) => (
            <div key={index}>
              <h2>{prof.name}</h2>
              <p>Rating: {prof.rating}</p>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default Results;
