import { Button, Column, FlexGrid, Form, InlineLoading, InlineNotification, Row, Stack, TextInput, Link } from "@carbon/react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function UserLogin({cookies, setCookie, removeCookie}) {
    const navigate = useNavigate();
    const [userID, setUserID] = useState('');
    const [password, setPassword] = useState('');
    const [isSubmitting, setIsSubmitting] = useState(false);
    const [status, setStatus] = useState('inactive');
    const [description, setDescription] = useState('Logging in');
    const [ariaLive, setAriaLive] = useState('off');

    const HandleLogin = (e) => {
        e.preventDefault();
        setIsSubmitting(true);
        setStatus('active');
        setAriaLive('assertive');
        console.log("ID..",userID);
        console.log("password...",password);
        fetch(`http://localhost:8000/user-login/?username=${userID}&password=${password}`, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
            },
            mode: 'cors',
        }).then(async response => {
            if (response.status === 200) {
                const data = await response.json()
                setCookie('session_key', data.access_token)
                setCookie('username', data.username)
                navigate('/profile');
            } else {
                setIsSubmitting(false);
                setStatus('inactive');
                setDescription('Login failed');
            }
        })
    }

    return(
        <div className="user-login-padding">
            <FlexGrid>
                <Row>
                    <Column lg={8}>
                        <Form className="login-form" onSubmit={HandleLogin}>                
                            <Stack gap={7}>  
                                <div>
                                <h3>Log in</h3>
                                <div style={{paddingTop:'5px'}}>Don't have an account? <Link href="/signup">Create an account</Link></div>
                                </div>
                                
                                <TextInput labelText='Check your medical' placeholder="Enter patient ID" value={userID} onChange={(e) => setUserID(e.target.value)} required/>
                                <TextInput.PasswordInput labelText='Password' placeholder="******" value={password} onChange={(e) => setPassword(e.target.value)} required/>
                                <Link href="#">Forgot ID?</Link>
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
                                aria-label="closes notification"
                                onClose={function noRefCheck(){}}
                                onCloseButtonClick={function noRefCheck(){}}
                                statusIconDescription="notification"
                                title="Login failed"
                                subtitle="check your id or password"
                                />
                                }
                            </Stack>
                        </Form>
                    </Column>
                    <Column lg={8}>
                        <div>
                            <img className="user-login-img" src="images/medical-app.png" alt="Health stickers created by Stickers - Flaticon"/>
                        </div>
                    
                        <div style={{paddingTop:'2rem'}}>
                            All you patient health reports, audio transcripts and <br/>
                            meeting details in one place.
                        </div>
                    </Column>
                </Row>
            </FlexGrid>
            
            
        </div>
    )
}