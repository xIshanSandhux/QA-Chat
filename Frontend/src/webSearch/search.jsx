import { useState } from 'react';
export default function Search({webSearch, setWebSearch}){
    
    return (
        <div>
            <input type="checkbox" id="webSearch" checked={webSearch} onChange={() => setWebSearch(!webSearch)}/>
            <label htmlFor="webSearch">Web Search</label>
        </div>
    );
}