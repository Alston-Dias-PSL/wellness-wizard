import { FormItem, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button } from "@carbon/react"
import { useState } from "react"

export default function ReportSummary() {
    const [file, setFile] = useState(null);
    
    const handleFileChange = (e) => {
        if (e.target.files) {
            setFile(e.target.files[0]);
        }
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        console.log("file....", file)
    }

    return(
        <div className="report-summary-padding">
            <h3>Report Summary</h3>
            <Grid>
                <Column lg={16}>
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
            </Column>
            </Grid>
            <Grid>
                <Column lg={16}>
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
            </Grid>
        </div>
    )
}