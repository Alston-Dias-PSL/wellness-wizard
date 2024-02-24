import { FormItem, Row, MultiSelect, FileUploaderDropContainer, Grid, Column, FileUploaderItem, Button, Stack } from "@carbon/react"
import { useState } from "react"

export default function Doctor() {
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
        <Column lg={3} >
            <img src='https://plus.unsplash.com/premium_photo-1664475450083-5c9eef17a191?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8ZmVtYWxlJTIwZG9jdG9yfGVufDB8fDB8fHww' alt="Girl in a jacket" width="90" height="90"></img>
        </Column>
        <Column lg={6} >
            <h3>Dr Jane Dias</h3>
            <p>Specialty: <b>ENT</b></p>

        </Column>
        <Column lg={3}>
            <br></br>
            <Button>Book Appointment</Button>
        </Column>
    </Row>
    )
}