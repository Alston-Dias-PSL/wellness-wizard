import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"

export default function Disease(props) {

    const items = ['a', 'b', 'c'];

    return (
        <Column className="col-bottom" lg={8}>
        <h4> <u>{props.dname}</u></h4>
        <h2>Respiratory Infection</h2>
        <div className="d-border">
        <img className="pic-style" src="images/disease.jpeg" width="150" height="150"></img>
        <p className="d-border">
       Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum</p>                 
        </div>
    </Column>
    )
}