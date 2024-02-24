import { FormItem, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button } from "@carbon/react"
import { useState, useEffect } from "react"

function CursorSVG() {
    return (
      <svg
        viewBox="8 4 8 16"
        xmlns="http://www.w3.org/2000/svg"
        className="cursor"
      >
        <rect x="10" y="6" width="4" height="12" fill="#fff" />
      </svg>
    );
}

export default function ReportSummary() {
    const [file, setFile] = useState(null);
    const [apiResponse, setApiResponse] = useState(false);
    const [chatHistory, setChatHistory] = useState('"You are a friendly female therapist named Casey. Your knowledge is limited to therapy. You are not able to comment on anything else. Your mission is to improve the mental well-being of anyone that talks to you."')
    
    const [completedTyping, setCompletedTyping] = useState(false);
    
    const ReturnResponse = ({response}) => {
        const [displayResponse, setDisplayResponse] = useState("");
        useEffect(() => {
            let index =0;
            const intervalId = setInterval(() => {
                if(index < response.length) {
                    setDisplayResponse(prevResponse => prevResponse + response.charAt(index) );
                    index++;
                }else{
                    clearInterval(intervalId);
                }
            }, 20);
            
            return () => clearInterval(intervalId);
        }, [response]);

        return(
            <div>
                {displayResponse}
            </div>
        )
    }

    const handleFileChange = (e) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("file....", file)
        setApiResponse(true);
    }

    return(
        <div className="report-summary-padding">
            <h3>Report Summary</h3>
            <Grid>
                <Column lg={8}>
            <FormItem className="align-upload-center">
                <p className="cds--file--label">Upload files</p>
                <p className="cds--label-description">
                    Max file size is 5Mb. Supported file types are .jpg and .png.
                </p>
                <FileUploaderDropContainer
                    className="file-location"
                    accept={['application/pdf','audio/mp3,audio/*']}
                    innerRef={{current: '[Circular]'}}
                    labelText="Drag and drop a file here or click to upload"
                    name="{setFileName(name)}"
                    disabled={false}
                    multiple={false}
                    onAddFiles={(e) => setFile(e.target.files[0])}
                />
                <div className="cds--file-container cds--file-container--drop" />
            </FormItem>
            {file &&
            <div>
                <div>
                <FileUploaderItem
                errorBody="500kb max file size. Select a new file and try again."
                errorSubject="File size exceeds limit"
                iconDescription="Delete file"
                name={file.name}
                onDelete={()=>setFile(null)}
                size="lg"
                status='edit'
                />
                </div>
                <div>
                    <Button style={{alignItems:'center'}} type="submit" size="md" onClick={handleSubmit}>Submit Report</Button>
                </div>

            </div>
            }
            </Column>
            <Column lg={8}>
            <div>
                {apiResponse &&
                <ReturnResponse response={chatHistory}/>
                }
            </div>
            </Column>
            </Grid>
        </div>
    )
}