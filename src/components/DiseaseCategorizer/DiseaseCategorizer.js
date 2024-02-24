import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"
import Doctor from "../Doctor/Doctor";

export default function DiseaseCategorizer() {
    // const [file, setFile] = useState(null);

    // const handleFileChange = (e) => {
    //     if (e.target.files) {
    //         setFile(e.target.files[0]);
    //     }
    // }

    // const handleSubmit = (e) => {
    //     e.preventDefault();
    //     console.log("file....", file)
    // }
    const items = ['a', 'b', 'c'];
    const [dp, setDp] = useState('none');

    const handleSubmit = (e) => {
        // e.preventDefault();
        // console.log("file....", file)
        // setApiResponse(true);

        setDp('true');
    }


    return (
        <div className="categorizer-padding">
            {/* <h3>Disease Categorizer</h3> */}
            <Grid>
                
                    <Column lg={16}>

                        <div className="category-row">
                           
                            
                            <MultiSelect label="Add symptoms for diagnosis" id="carbon-multiselect-example" items={items} selectionFeedback="top-after-reopen" />
                              
                              <Button className="s-bt" size="md" onClick={handleSubmit}>Diagnose</Button>              
                           
                                
                            

                        </div>


                    </Column>
            </Grid>

            <Grid className="bottom-div">
                

              
                    {dp == 'true' &&
                        <Column className="col-left" style={{ display: { dp } }} lg={8}>

                            <h4> <u>Diagnosis</u></h4>
                            <h2>Respiratory Infection</h2>
                            <div className="d-border">
                            <img src="images/disease.jpeg" width="150" height="150"></img>
                            <p className="d-border">
                           Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>                 
                            </div>
                        </Column>
                    }
                    {dp == 'true' &&
                        <Column style={{ display: { dp } }} lg={8}>
                            <h3>Doctors available for consultation</h3>
                            <Doctor></Doctor>
                        </Column>
                    }
               

            </Grid>
        </div>
    )
}