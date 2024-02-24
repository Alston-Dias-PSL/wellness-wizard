import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"
import Doctor from "../Doctor/Doctor";
import Disease from "../Disease/Disease";

export default function DiseaseCategorizer() {

    const items = ['a', 'b', 'c'];
    const [dp, setDp] = useState('none');

    const handleSubmit = (e) => {
        setDp('true');
    }


    return (
        <div className="categorizer-padding">
          
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
<Disease dname="Respiratory Infection"></Disease>
                    }
                    {dp == 'true' &&
                        <Column className="col-bottom" style={{ display: { dp } }} lg={8}>
                            <h3>Doctors available for consultation</h3>
                            <Doctor name="Dr Pritam " spec="ENT"></Doctor>
                            <Doctor name="Dr Alston " spec="Ortho"></Doctor>
                        </Column>
                    }
               

            </Grid>
        </div>
    )
}