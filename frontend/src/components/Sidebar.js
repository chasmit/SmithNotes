import React from "react";
import { useNavigate } from "react-router-dom"
import { Button, ButtonGroup, Navbar } from "reactstrap";

import { FaHouseChimney, FaPlus } from "react-icons/fa6";

function Sidebar() {
    const navigate = useNavigate();

    const goToNoteGrid = () => {
        navigate("/");
    }

    const goToAddNoteForm = () => {
        navigate("/form", {state:{id:null}});
    }

    return ( 
        <Navbar className="app-sidebar">
            <ButtonGroup>
            <Button className="app-button" onClick={ goToNoteGrid }>
                Home {<FaHouseChimney/>}
            </Button>
            <Button className="app-button" onClick={ goToAddNoteForm }>
                Add Note {<FaPlus/>}
            </Button>
            </ButtonGroup>
        </Navbar>   
    )
}

export default Sidebar;