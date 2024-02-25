import {
  FormItem,
  FileUploaderDropContainer,
  Grid,
  Column,
  FileUploaderItem,
  Button,
} from "@carbon/react";
import { CloudUpload } from "@carbon/pictograms-react";
import { ReminderMedical, Rocket } from "@carbon/icons-react";
import { useState, useEffect } from "react";

// const chatResponse = "Assesment and Plan Mary Smith aged 68 has been diagnosed with metastatic \
// breast cancer. She has recieved chemotherapy, radiation therapy and surgical intervention to manage \
// a disease, but is declining in function and experiencing increased symptoms everyday. She wishes to \
// spend her remaining time at home surrounded by family. Her medical support plan includes optimising \
// analgesic therapy, addressing other symptoms, and providing emotional and psychological support"

// const fileContent = "Chief Complaint:\
// The patient presents with a one-week history of persistent headache and occasional dizziness.\
// History of Present Illness:\
// Mr. Doe reports the onset of a dull, continuous headache localized to the frontal and temporal regions. He rates the pain intensity as 6/10 on a numerical scale. The headache is not alleviated by rest and is occasionally accompanied by dizziness, especially upon sudden position changes. He denies any recent head trauma, vision changes, or other focal neurological symptoms.\
// Past Medical History:\
// Hypertension, diagnosed in 2010, controlled with medication (lisinopril 20 mg daily) Allergies: None known Surgeries: Appendectomy in 1995 Medications: Lisinopril, as mentioned; no other regular medications\
// Family History:\
// Father: Hypertension Mother: Type 2 diabetes No family history of neurological disorders\
// Social History: Mr. Doe is a non-smoker and consumes alcohol occasionally. He denies any recreational drug use. He is married with two children and works as an accountant."

export default function ReportSummary(cookies) {
  const [file, setFile] = useState(null);
  const [chatHistory, setChatHistory] = useState(
    "Upload a pdf or audio file of your medical report to get the summary."
  );
  const [uploadedFileContent, setUploadFileContent] = useState("");
  const [isFileUploaded, setIsFileUploaded] = useState(false);
  const [chatResponse, getChatResponse] = useState("");
  const [fileContent, getFileContent] = useState("");

  const ReturnResponse = ({ response }) => {
    const [displayResponse, setDisplayResponse] = useState("");
    useEffect(() => {
      let index = 0;
      const intervalId = setInterval(() => {
        if (index < response.length) {
          setDisplayResponse(
            (prevResponse) => prevResponse + response.charAt(index)
          );
          index++;
        } else {
          clearInterval(intervalId);
        }
      }, 20);

      return () => clearInterval(intervalId);
    }, [response]);

    return (
      <div className="typing-response">
        <div className="chat-bubble chat-bubble-font">{displayResponse}</div>
      </div>
    );
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("files", file);
    if (file.name.endsWith("pdf")) {
      const API_NAME = "generate-report-summary";

      fetch(`http://localhost:8000/${API_NAME}/?token=${cookies.cookie['session_key']}`, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          getChatResponse(data.summary);
          getFileContent(data.pdf_text);
          setChatHistory(data.summary);
        })
        .catch((error) => {
          console.error("There was an error with the upload:", error);
        });
    } else {
      const API_NAME = "upload-audio";
      fetch(`http://localhost:8000/${API_NAME}/?token=${cookies.cookie['session_key']}`, {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (!response.ok) {
            throw new Error("Response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          getChatResponse(data.summary);
          getFileContent(data.transcript);
          setChatHistory(data.summary);
        })
        .catch((error) => {
          console.error("There was an error with the upload:", error);
        });
    }

    // setChatHistory(chatResponse);
  };

  return (
    <div className="report-summary-padding">
      <div style={{ backgroundColor: "rgba(256 , 256,256,0.5)" }}>
        <div
          style={{
            paddingInlineStart: "2rem",
            color: "black",
            display: "inline-flex",
          }}
        >
          <h3>Medical Report Summary</h3>&nbsp;
          <ReminderMedical size={32} />
        </div>
        <Grid className="grid-style">
          <Column lg={8} className="column-1">
            <FormItem className="align-upload-center">
              <p className="cds--file--label">Upload files</p>
              <p className="cds--label-description">
                Max file size is 5Mb. Supported file types are .jpg and .png.
              </p>
              <div>
                {isFileUploaded && (
                  <div className="input-bubble">{fileContent}</div>
                )}
                <FileUploaderDropContainer
                  className="file-location"
                  accept={["application/pdf", "audio/mp3,audio/*"]}
                  innerRef={{ current: "[Circular]" }}
                  labelText={
                    <div>
                      Drag and drop a file here or click to upload{" "}
                      <CloudUpload />
                    </div>
                  }
                  name=""
                  disabled={false}
                  multiple={false}
                  onAddFiles={(e) => {
                    setFile(e.target.files[0]);
                    setChatHistory("Ssubmit to generate result");
                    setIsFileUploaded(true);
                  }}
                />
              </div>
              <div className="cds--file-container cds--file-container--drop" />
            </FormItem>
            {file && (
              <div style={{ paddingTop: "1rem" }}>
                <div>
                  <FileUploaderItem
                    errorBody="5Mb max file size. Select a new file and try again."
                    errorSubject="File size exceeds limit"
                    iconDescription="Delete file"
                    name={file.name}
                    onDelete={() => {
                      setFile(null);
                      setChatHistory(
                        "Uppload a pdf or audio file of your medical report to get the summary."
                      );
                      setIsFileUploaded(false);
                    }}
                    size="lg"
                    status="edit"
                  />
                </div>
              </div>
            )}
          </Column>
          {isFileUploaded && (
            <Column lg={1} className="column-2">
              <Button
                tooltipPosition="bottom"
                type="submit"
                onClick={handleSubmit}
                size="lg"
                renderIcon={() => <Rocket size={24} />}
                iconDescription="Submit"
                hasIconOnly
              />
            </Column>
          )}
          <Column className="column-3" lg={7}>
            <div>
              <ReturnResponse response={chatHistory} />
            </div>
          </Column>
        </Grid>
      </div>
    </div>
  );
}
