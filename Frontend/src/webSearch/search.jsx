import { useState } from 'react';
export default function Search({rag, setRag}){
    
    return (
        <div>
            <input type="checkbox" id="webSearch" checked={rag} onChange={() => setRag(!rag)}/>
            <label htmlFor="webSearch">RAG</label>
        </div>
    );
}