import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"
import Doctor from "../Doctor/Doctor";
import Disease from "../Disease/Disease";

export default function DiseaseCategorizer() {

    const items = ['Cough', 'Wheeze', 'Labored breathing'];
    const [dp, setDp] = useState(false);

    const handleSubmit = (e) => {
        setDp(true);
    }
    
    return (
        <div className="categorizer-padding"> 
            <h3>Disease categorizer</h3>
                <div style={{paddingBottom:'1rem'}}> 
                    <div>
                    <MultiSelect label="Add symptoms for diagnosis" id="carbon-multiselect-example" items={items} selectionFeedback="top-after-reopen" />
                    </div>
                    <div style={{paddingTop:'1rem'}}>
                    <Button size="md" onClick={handleSubmit}>Diagnose</Button>
                    </div>                       
                </div>
                {dp &&
                <Grid narrow>
                <Column lg={8}>
                    <Disease dname="Respiratory Infection"/>
                </Column>
                <Column lg={8}>
                    <h3 style={{color:'black'}}>Doctors available for consultation</h3>
                    <Doctor name="Dr Pritam " spec="ENT"/>
                    <Doctor name="Dr Alston " spec="Ortho"/>
                </Column>
                </Grid>
                }
                
        </div>
    )
}