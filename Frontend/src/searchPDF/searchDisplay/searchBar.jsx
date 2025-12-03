import './searchBar.css';
import {useState} from 'react';
import { IoIosSearch } from "react-icons/io";
export default function SearchBar(){

    const [search, setSearch] = useState("");
    // console.log(search);

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
            {/* TODO: create function to update the results count based on the chunks received from backend. 
            Maybe have "---" as the default value ? Maybe have a loading state ?*/}
            {/* TODO: dsiplay the search results in a list format */}
        </div>
    )
}