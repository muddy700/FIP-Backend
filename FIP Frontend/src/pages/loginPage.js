import React, { useState} from 'react'
import { Form, Button } from 'react-bootstrap'
import '../styles/loginPage.css'

export const LoginPage = () => {

    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const onFinish = (e) => {
        // e.preventDefault()
        console.log(username, password)
    }

    return (
        
        <div className="login-form-container">
            <form className="login-form" onsubmit={e => { e.preventDefault(); onFinish(e) }}>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>Username</Form.Label>
                    <Form.Control type="text" name="username" value={username} onChange={e => setUsername(e.target.value)} placeholder="Enter Username" />
                </Form.Group>

                <Form.Group controlId="formBasicPassword">
                    <Form.Label>Password</Form.Label>
                        <Form.Control type="password" name="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="Password" />
                </Form.Group>
                <Button variant="primary" type="submit">
                    Login
                </Button>
            </form>
        </div>
    )
}
