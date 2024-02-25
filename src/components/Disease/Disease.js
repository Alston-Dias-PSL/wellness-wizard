import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"

export default function Disease(props) {

    const items = ['a', 'b', 'c'];

    return (
        <Column className="col-bottom" lg={8}>
        <div style={{display:'inline-flex', alignItems:'center', paddingBottom:'1rem'}}><h6>{props.dname}:</h6> <h3 style={{color:'black'}}>Respiratory Infection</h3></div>   
        <div className="d-border">
        <p className="d-border" style={{color:'black'}} >
        Based on the symptoms you provided, 
        it's indicative of a respiratory condition commonly associated with asthma. 
        Asthma is a chronic inflammatory disorder of the airways characterized by episodes of wheezing, 
        breathlessness, chest tightness, and coughing, especially at night or early morning. 
        It's often triggered by factors such as allergens, exercise, cold air, or respiratory infections. 
        Proper diagnosis and management by a healthcare professional are crucial for effectively managing asthma symptoms and preventing exacerbations.              
        </p>
        </div>
    </Column>
    )
}