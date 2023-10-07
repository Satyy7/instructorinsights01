import React, {useState} from "react";
import axios from 'axios';
import "./Filter.css";
import Results from "../results/Results";

function Filter() {

  const [department, setDepartment] = useState('');
  const [rating, setRating] = useState('');
  const [ratingCount, setRatingCount] = useState('')
  const [wta, setWta] = useState('')
  const [results, setResults] = useState([]);

  const handleClick = async () => {
    const response = await axios.post('http://127.0.0.1:5000/query', {
      department,
      rating,
      ratingCount,
      wta
    });
    setResults(response.data)
    console.log(response.data);
  }



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
              onChange={(e) => setDepartment(e.target.value)}
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
              onChange={(e) => setRating(e.target.value)}
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
              onChange={(e) => setRatingCount(e.target.value)}
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
              onChange={(e) => setWta(e.target.value)}
            />
          </form>
        </div>
        <button className="filter-button" onClick={handleClick}>Query</button>
      </div>
      <Results data = {results}/>
    </>
  );
}

export default Filter;
