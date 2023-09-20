import { FaGithub, FaLinkedin, FaEnvelope } from 'react-icons/fa';
import { profileLinks } from '../../config';
import './index.css';

const Footer = () => {
    const { linkedin, github, email } = profileLinks;
    
    return (
        <footer className="footer">
            <span className="text">Created by Brad Simpson ©2022</span>
            <a href={github} >
                <FaGithub className="icons"/>
            </a>
            <a href={linkedin} >
                <FaLinkedin className="icons" />
            </a>
            <a href={`mailto:${email}`}>
                <FaEnvelope className="icons" />
            </a> 
        </footer>
)};

export default Footer;