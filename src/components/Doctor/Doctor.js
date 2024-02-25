import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"
import ChatBot from '../ChatBot/ChatBot';

export default function Doctor(props) {
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

    return (
        <Row id='d-row'>
        <Column md={4} >
            <img className="pic-style" src='https://plus.unsplash.com/premium_photo-1664475450083-5c9eef17a191?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZmVtYWxlJTIwZG9jdG9yfGVufDB8fDB8fHww' alt="Girl in a jacket" width="90" height="90"></img>
        </Column>
        <Column md={3} >
            <h3>{props.name}</h3>
            <p>Specialty: <b>{props.spec}</b></p>
        </Column>
        <Column md={1}>
            <br></br>
            <Button>Book Appointment using AI</Button>
        </Column>
        <ChatBot/>
    </Row>
    )
}