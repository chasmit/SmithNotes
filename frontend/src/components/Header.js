import { FaFileCircleCheck } from "react-icons/fa6";

function Header() {
    return (
        <h2 className="app-header">
            Notes App {<FaFileCircleCheck className="fa-xl"/>} 
        </h2>
    )
}

export default Header;