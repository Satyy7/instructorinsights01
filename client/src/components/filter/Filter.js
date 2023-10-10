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
      department: department,
      rating: rating,
      ratingCount: ratingCount,
      wta: wta,
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
              placeholder="Enter a number 1-5"
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
              placeholder="Enter a number"
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
              placeholder="Enter a number"
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
