import './app.scss';
import { BrowserRouter, Routes, Route, Navigate} from 'react-router-dom';
import { useCookies} from 'react-cookie';
import { useEffect, useState } from 'react';
import { Theme, GlobalTheme } from '@carbon/react';

import NavBar from './components/NavBar';
import UserLogin from './components/UserLogin/UserLogin';
import Signup from './components/UserLogin/Signup';
import Profile from './components/Profile/Profile';
import ReportSummary from './components/ReportSummary/ReportSummary';
import DiseaseCategorizer from './components/DiseaseCategorizer/DiseaseCategorizer';

function App() {
    const [globaltheme,setGlobaltheme] = useState('g100');
    const [cookies, setCookie, removeCookie] = useCookies(['session_key', 'username'])

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
                <Route path="/" element={<NavBar setTheme={setTheme}  />}>
                    <Route index element={<UserLogin cookies={cookies} setCookie={setCookie} removeCookie={removeCookie} />} />
                    <Route path='/login' element={<UserLogin/>} />
                    <Route path='/signup'element={<Signup/>}/>
                    <Route path='/profile' element={<Profile/>}/>
                    <Route path='/report-summary' element={<ReportSummary cookies={cookies}/>} />
                    <Route path='/disease-categorizer' element={<DiseaseCategorizer/>} />
                </Route>
            </Routes>
        </BrowserRouter>
        </GlobalTheme>
    );
}

export default App;
