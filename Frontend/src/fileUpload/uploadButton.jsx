import { useRef, useEffect } from 'react';
import './uploadFile.css';
import axios from 'axios';
import Cookies from 'js-cookie';

export default function UploadButton(){
    const fileInputRef = useRef(null);
    const sessionId = Cookies.get('sessionId');
    console.log(sessionId);
    console.log('sessionId', sessionId);
    // useEffect(()=>{
    const handleFileUpload = async (e) => {
        console.log('handleFileUpload');
        console.log(e);
        const files = e.target.files;
        if (files.length===0 || !files) return;
        console.log(e.target);

        const curFile = files[0];
        const formData = new FormData();
        formData.append('pdfFile', curFile);
        formData.append('sessionId', sessionId);

        
        try{
            const uploading = await pdfUpload(formData);
            console.log(uploading);
        }catch(error){
            console.error('Error uploading PDF:', error);
        }finally{
            fileInputRef.current.value = '';
        }

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

async function pdfUpload(formData){
    let response;
    try{
        response = await axios.post('http://127.0.0.1:8000/pdfUpload', formData);
        console.log(response.data);
    }catch(error){
        console.error('Error uploading PDF:', error);
    }
    return response.data.message;
}