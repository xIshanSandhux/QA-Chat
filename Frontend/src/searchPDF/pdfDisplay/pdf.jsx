import './pdf.css';
import axios from 'axios';
import { useRef, useState } from 'react';
import Cookies from 'js-cookie';
import UploadButton from '../../fileUpload/uploadButton';

export default function PdfDisplay(){

    const fileInputRef = useRef(null);
    const [fileCount, setFileCount] = useState(0);
    console.log()

    const fileUpload = async(e)=>{

        const file = e.target.files;

        if(!file) return;

        setFileCount(file.length);
        const curFile = file[0];
        const fileFormData = new FormData();
        fileFormData.append('pdfFile', curFile);
        fileFormData.append('sessionId', "test-1234");
        
        try{
            const res = await pdfUpload(fileFormData);
            console.log(res);
        }catch(error){
            console.error('Error uploading PDF:', error);
        }finally{
            fileInputRef.current.value = '';
        }
        // console.log(e.target.files[0].name);
        // console.log(await e.target.files.length);
        // return await e.target.files.length;
    }

    const clickUploadButton = () =>{
        if(!fileInputRef.current) return;
        fileInputRef.current.click();
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
            <button className="pdf-upload-button" onClick={clickUploadButton}>Upload PDF</button>
            // <UploadButton sessionId="sddjdjd" />
            // <h1>Upload PDF hello</h1> 
            :
            <>
            <button className="pdf-upload-button" onClick={clickUploadButton}>Upload PDF</button>
            <h1>PDF Display</h1>
            </> 
            }
        </div>
    );
}

async function pdfUpload(fileFormData){
    let response;
    try{
        response = await axios.post('http://127.0.0.1:8000/pdfUpload', fileFormData);
        console.log(response.data);
    }catch(error){
        console.error('Error uploading PDF:', error);
    }
    Cookies.set('curFile', response.data.curFile);
    return response.status;
}