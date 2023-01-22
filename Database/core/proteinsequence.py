import sdRDM

from typing import Optional, Union
from typing import List
from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .database import Database
from .organism import Organism


@forge_signature
class ProteinSequence(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinsequenceINDEX"),
        xml="@id",
    )

    protein_sequence_id: Optional[str] = Field(
        description="Presented protein sequence", default=None
    )

    name: Optional[str] = Field(
        description="Systematic name of the protein.", default=None
    )

    amino_acid_sequence: Optional[str] = Field(
        description="The amino acid sequence of the protein sequence object.",
        default=None,
    )

    pdb_id: List[str] = Field(
        description="Identifier for the PDB database", default_factory=ListPlus
    )

    protein_database_id: Optional[Database] = Field(
        description="Data base ID", default=None
    )

    protein_database_entry: Optional[str] = Field(
        description="Identifier for the database", default=None
    )

    protein_organism_id: Optional[Organism] = Field(
        description="Corresponding organism", default=None
    )

    index: Optional[int] = Field(description="indexing method", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/maxim945/PyEED-Fullprototype.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="554d49fe10c158c6d8dd7a018c6798092777529d"
    )
