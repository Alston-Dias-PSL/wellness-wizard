import './app.scss';
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import { useCookies } from 'react-cookie';
import { useEffect, useState } from 'react';
import { Theme, GlobalTheme } from '@carbon/react';

import NavBar from './components/NavBar';
import UserLogin from './components/UserLogin/UserLogin';
import Signup from './components/UserLogin/Signup';
import Profile from './components/Profile/Profile';

function App() {
    const [globaltheme,setGlobaltheme] = useState('g100');

    useEffect(() => {
        document.documentElement.dataset.carbonTheme = globaltheme;
    }, [globaltheme]);

    const setTheme = () =>{
        if(globaltheme === "g100"){
            setGlobaltheme('white');
        }
        if(globaltheme === "white"){
            setGlobaltheme('g100')
        }
    }

    return (
        <GlobalTheme theme={globaltheme}>
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<NavBar setTheme={setTheme}/>}>
                    <Route index element={<UserLogin/>} />
                    <Route path='/login' element={<UserLogin/>} />
                    <Route path='/signup'element={<Signup/>}/>
                    <Route path='/Profile' element={<Profile/>}/>
                </Route>
            </Routes>
        </BrowserRouter>
        </GlobalTheme>
    );
}

export default App;
