import React from "react";
import "./Results.css";
function Results({ data }) {
  return (
    <>
      <div className="results-container"></div>
      <div className="results-header">Results</div>
      <div>
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Rating</th>
            </tr>
          </thead>
          <tbody>
            {data.map((prof, index) => (
              <tr
                className={index % 2 === 0 ? "even-row" : "odd-row"}
                key={index}
              >
                <td>{prof.name}</td>
                <td>Rating: {prof.rating}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </>
  );
}

export default Results;
