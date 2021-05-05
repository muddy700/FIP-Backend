import React from 'react'
import { Redirect, Route } from 'react-router-dom';
import {useSelector} from 'react-redux'
import { selectUserData } from '../slices/userSlice'

export const PrivateRoute = ({ component: Component, ...rest }) => {
    const user = useSelector(selectUserData);
    let isLoggedIn = user.isAuthenticated
    return (
        <Route {...rest} render={props => isLoggedIn ? (
            <Component {...props} /> ) : 
            (<Redirect to="/login" />)} />
    )
}
