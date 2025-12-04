import './searchBar.css';
import {useState} from 'react';
import { IoIosSearch } from "react-icons/io";
export default function SearchBar(){

    const [search, setSearch] = useState("");
    // const [selected, setSelected] = useState(null);
    // console.log(search);
    const dummyResults = [
        { "page": 1, "data": "Introduction to machine learning and problem definition." },
        { "page": 1, "data": "Overview of supervised vs unsupervised learning." },
        { "page": 2, "data": "Linear regression formula derivation and assumptions." },
        { "page": 2, "data": "Example dataset explanation with feature variables." },
        { "page": 3, "data": "Gradient descent algorithm steps and intuition." },
        { "page": 4, "data": "RRegularization methods: L1 and L2 comparison.eRegularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.Regularization methods: L1 and L2 comparison.gularization methods: L1 and L2 comparison." },
        { "page": 5, "data": "Regularization methods: L1 and L2 comparison." },
        { "page": 6, "data": "Regularization methods: L1 and L2 comparison." },
        { "page": 7, "data": "Regularization methods: L1 and L2 comparison." },
        { "page": 8, "data": "Regularization methods: L1 and L2 comparison." },
        { "page": 9, "data": "Regularization methods: L1 and L2 comparison." },
        { "page": 10, "data": "Model evaluation metrics: accuracy, precision, recall." }
    ];


    return (
        <div className="search-main-container">
            <form 
            name="search-bar-form"
            className="search-bar-main-container"
            onSubmit={(e)=>{
                e.preventDefault();
                console.log(search);
                setSearch("");
                // will be sending the query to the backend
                // need to get the backend working for it but will be doing console log until then
            }}
            >
                <textarea
                className="search-bar-input"
                type="text"
                spellCheck="true"
                placeholder="Search in PDF..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                />

                <button 
                className="search-bar-button"
                type="submit"
                disabled={!search.trim()}
                >
                    <IoIosSearch size={30} color="#ffffff"/>
                </button>
            </form>

            <h3>PDF Search Results: ---</h3>

            <div
            className="search-results-container"
            >
                {dummyResults.map((result, index)=>{
                    console.log(result);
                  return (
                  <div 
                  className="search-result-item"
                    key={index}
                    // onClick={()=>setSelected(result)}
                    >
                        <p className="search-result-item-page">Page: {result.page}</p>
                        <p className="search-result-item-data">{result.data}</p>
                    </div>
                    )
                })}
            </div>
        </div>
    )
}