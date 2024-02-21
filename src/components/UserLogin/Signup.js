import { Button, Form, Stack, TextInput, Link, InlineLoading, InlineNotification } from "@carbon/react"
import { useState } from "react"

export default function Signup(){
    const [userName, setUserName] = useState('');
    const [password, setPassword] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const isValidPhone= /^[0-9]{10}$/.test(phoneNumber);
    const isValidPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,}$/.test(password)

    const [isSubmitting, setIsSubmitting] = useState(false);
    const [status, setStatus] = useState('inactive');
    const [description, setDescription] = useState('Logging in');
    const [ariaLive, setAriaLive] = useState('off');

    const HandleSignup= (e) => {
        e.preventDefault();
        console.log(userName)
        console.log(password)
        console.log(phoneNumber)
        console.log(isValidPassword)
        console.log(isValidPhone)
        setIsSubmitting(true);
        setStatus('active');
        setAriaLive('assertive');
    }
    return(
        <div className="user-login-padding">
            <Form className='login-form' onSubmit={HandleSignup}>
                <Stack gap={7}>
                    <div>
                        <h3>Log in</h3>
                        <div style={{paddingTop:'5px'}}>Already have an account? <Link href="/login">Log in</Link></div>
                    </div>
                    <TextInput labelText='Full name' id="name" value={userName} onChange={(e)=>setUserName(e.target.value)} required/>
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
        </div>
    )
}