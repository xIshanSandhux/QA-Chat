import './pdf.css';
import { useRef, useState } from 'react';
import UploadButton from '../../fileUpload/uploadButton';

export default function PdfDisplay(){

    const fileInputRef = useRef(null);
    const [fileCount, setFileCount] = useState(0);
    console.log()

    const fileUpload = async(e)=>{
        setFileCount(e.target.files.length);
        console.log(await e.target.files.length);
        return await e.target.files.length;
    }

    return (
        <div className="pdf-display">

            <input
            type="file"
            ref={fileInputRef}
            hidden={true}
            onChange={fileUpload}
            accept="application/pdf"
            />

            {fileCount===0? 
            <button className="pdf-upload-button" onClick={()=>fileInputRef.current.click()}>Upload PDF</button>
            // <UploadButton sessionId="sddjdjd" />
            // <h1>Upload PDF hello</h1> 
            : 
            <h1>PDF Display</h1>}
        </div>
    );
}