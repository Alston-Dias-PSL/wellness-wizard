import { Button, Form, Stack, TextInput, Link, InlineLoading, InlineNotification, Grid, Column, FlexGrid, Row } from "@carbon/react"
import { useState } from "react"

export default function Signup(){
    const [fname, setFname] = useState('');
    const [lname, setLname] = useState('');
    const [address, setAddress] = useState('');
    const [email, setEmail] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [password, setPassword] = useState('');
    const isValidPhone= /^[0-9]{10}$/.test(phoneNumber);
    const isValidPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/.test(password)

    const [isSubmitting, setIsSubmitting] = useState(false);
    const [status, setStatus] = useState('inactive');
    const [description, setDescription] = useState('Logging in');
    const [ariaLive, setAriaLive] = useState('off');

    const HandleSignup= (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        setStatus('active');
        setAriaLive('assertive');
    }
    return(
        <div className="user-login-padding">
            <Grid className='main-row'>
            <Column lg={8} className='signup-column verticle-line' >   
            <Form className='login-form' onSubmit={HandleSignup}>
                <Stack gap={4}>
                    <div>
                        <h3>Log in</h3>
                        <div style={{paddingTop:'5px'}}>Already have an account? <Link href="/login">Log in</Link></div>
                    </div>
                    <Grid>
                        <Column sm={4}>
                        <TextInput labelText='First name' id="fname" value={fname} onChange={(e)=>setFname(e.target.value)} required/>
                        </Column>
                        <Column sm={4}>
                        <TextInput labelText='First name' id="lname" value={lname} onChange={(e)=>setLname(e.target.value)} required/>
                        </Column>
                    </Grid>
                    <TextInput labelText='Address' id="address" value={address} onChange={(e)=>setAddress(e.target.value)} required/>
                    <TextInput labelText='Email ID' id="email" value={email} onChange={(e)=>setEmail(e.target.value)} required/>
                    <TextInput labelText="Phone number" type="tel" id="phone" 
                    invalid={!isValidPhone}
                    pattern="[0-9]{10}"
                    invalidText='Phone number should be 10 digit'
                    value={phoneNumber}
                    onChange={(e) => setPhoneNumber(e.target.value)}
                    required/>
                    <TextInput id="password" type="password" labelText='Password' required 
                    autoComplete="off"
                    pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    invalid={!isValidPassword}
                    invalidText = 'Your password must be at least 6 characters as well as contain at least one uppercase, one lowercase, and one number.' 
                    />

                    {isSubmitting ?
                        <InlineLoading
                        description={description}
                        status={status}
                        aria-live={ariaLive}
                        />:
                        <Button type="submit" tabIndex={7}>Log in</Button>
                    }
                    {isSubmitting && 
                        <InlineNotification
                        kind='success'
                        aria-label="closes notification"
                        onClose={function noRefCheck(){}}
                        onCloseButtonClick={function noRefCheck(){}}
                        statusIconDescription="notification"
                        title="Account created"
                        subtitle="Login with id and password"
                        />
                    }
                </Stack>
            </Form>
            </Column>
            <Column lg={8}>
                <h4 style={{paddingTop:'2rem', fontStyle:'bold', paddingBottom:'1rem', textAlign:'center'}}>
                    All you patient health reports, audio transcripts and <br/>
                    meeting details in one place.
                </h4>
                    <div style={{ textAlign:'center', paddingTop:'2rem' }}>
                    <img className="user-login-img" src="images/ehr-1476525_1280.png" alt="Health stickers created by Stickers - Flaticon"/>
                </div>
            </Column>
            </Grid>
        </div>
    )
}