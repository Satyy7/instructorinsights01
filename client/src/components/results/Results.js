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
            <div className="prof" key={index}>
              <div className="prof-name">
                <h2>{prof.name}</h2>
                </div>
              <p className="rating">Rating: {prof.rating}</p>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}

export default Results;
