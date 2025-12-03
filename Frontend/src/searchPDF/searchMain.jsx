import SearchBar from './searchDisplay/searchBar';
import PdfDisplay from './pdfDisplay/pdf';
import './searchMain.css';

export default function SearchMain(){
    return (
        <div className="search-main">
            <SearchBar />
            <PdfDisplay />
        </div>
    );
}

