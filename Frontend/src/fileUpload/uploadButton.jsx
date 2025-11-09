import { useRef } from 'react';
import './uploadFile.css';
export default function UploadButton(){
    const fileInputRef = useRef(null);

    const handleFileUpload = (e) => {
        const files = e.target.files;
        if (files.length===0 || !files) return;
        console.log(e.target);

        const curFile = files[0];
        console.log(curFile.name);
        console.log(curFile.type)
    }
    const onClickButton = () => {
        if(!fileInputRef.current) return;
        fileInputRef.current.click();
    }

    return (
        <div>
            <input ref={fileInputRef} type="file" accept="application/pdf" hidden onChange={handleFileUpload}  multiple />
            <button onClick={onClickButton} className="upload-button">Upload</button>
        </div>
    )
}