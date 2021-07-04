from djangosaml2_spid.spid_attributes import SPID_ATTRIBUTES

ATTRS = [
    'facsimileTelephoneNumber',
    'postalAddress',
    'schacProjectMembership',
    'matricola_dipendente',
    'schacProjectSpecificRole',
    'physicalDeliveryOfficeName',
    'departmentNumber',
    'eduPersonUniqueId',
    'PVP-CHARGE-CODE',
    'dmdName',
    'enhancedSearchGuide',
    'displayName',
    'street',
    'D-2012-17-EUIdentifier',
    'preferredDeliveryMethod',
    'co',
    'eduPersonScopedAffiliation',
    'eduPersonOrgDN',
    'DateOfBirth',
    'telephoneNumber',
    'authorityRevocationList',
    'norEduPersonLegalName',
    'LegalName',
    'carLicense',
    'schacPersonalUniqueCode',
    'userCertificate',
    'PVP-INVOICE-RECPT-ID',
    'crossCertificatePair',
    'osiOtherHomePhone',
    'postOfficeBox',
    'serialNumber',
    'eduPersonOrcid',
    'osiHomeUrl',
    'employeeType',
    'mail',
    'eduPersonAffiliation',
    'schacHomeOrganization',
    'norEduPersonBirthDate',
    'userPKCS12',
    'uid',
    'osiWorkURL',
    'schacExpiryDate',
    'norEduOrgUniqueNumber',
    'EORI',
    'eduPersonTargetedID',
    'eduPersonEntitlement',
    'registeredAddress',
    'schacSn1',
    'presentationAddress',
    'norEduOrgUniqueIdentifier',
    'deltaRevocationList',
    'schacUserStatus',
    'schacSn2',
    'schacCountryOfCitizenship',
    'associatedDomain',
    'destinationIndicator',
    'x121Address',
    'supportedApplicationContext',
    'PVP-OU-OKZ',
    'cn',
    'PVP-VERSION',
    'norEduOrgNIN',
    'dc',
    'member',
    'owner',
    'sisLegalGuardianFor',
    'labeledURI',
    'searchGuide',
    'givenName',
    'x500UniqueIdentifier',
    'cACertificate',
    'schacPlaceOfBirth',
    'o',
    'sn',
    'schacPersonalUniqueID',
    'SEED',
    'schacPersonalTitle',
    'norEduOrgAcronym',
    'uniqueMember',
    'postalCode',
    'PersonIdentifier',
    'employeeNumber',
    'norEduPersonNIN',
    'teletexTerminalIdentifier',
    'osiPreferredTZ',
    'eduPersonPrincipalName',
    'pseudonym',
    'PVP-BIRTHDATE',
    'norEduOrgUnitUniqueIdentifier',
    'roleOccupant',
    'osiMiddleName',
    'initials',
    'PVP-ROLES',
    'mail',
    'c',
    'businessCategory',
    'houseIdentifier',
    'BusinessCodes',
    'PVP-GID',
    'schacGender',
    'federationFeideSchemaVersion',
    'norEduOrgSchemaVersion',
    'schacCountryOfResidence',
    'CurrentAddress',
    'eduPersonPrimaryAffiliation',
    'schacHomeOrganizationType',
    'schacUserPrivateAttribute',
    'VATRegistration',
    'PVP-BPK',
    'LegalPersonIdentifier',
    'LEI',
    'LegalAddress',
    'eduCourseOffering',
    'schacDateOfBirth',
    'eduPersonPrimaryOrgUnitDN',
    'generationQualifier',
    'schacMotherTongue',
    'BirthName',
    'PVP-PARTICIPANT-OKZ',
    'schacUserPresenceID',
    'matricola_studente',
    'PVP-COST-CENTER-ID',
    'eduPersonOrgUnitDN',
    'TaxReference',
    'PVP-PRINCIPAL-NAME',
    'jpegPhoto',
    'eduPersonAssurance',
    'PVP-FUNCTION',
    'eduPersonNickname',
    'osiICardTimeLastUpdated',
    'knowledgeInformation',
    'eduCourseMember',
    'l',
    'internationaliSDNNumber',
    'userSMIMECertificate',
    'preferredLanguage',
    'supportedAlgorithms',
    'SIC',
    'norEduOrgUnitUniqueNumber',
    'isMemberOf',
    'dnQualifier',
    'protocolInformation',
    'osiOtherEmail',
    'codice_fiscale',
    'PVP-PARTICIPANT-ID',
    'title',
    'FirstName',
    'ou',
    'eduPersonPrincipalNamePrior',
    'PVP-OU-GV-OU-ID',
    'telexNumber',
    'norEduPersonLIN',
    'sisSchoolGrade',
    'schacPersonalPosition',
    'st',
    'certificateRevocationList'
] + SPID_ATTRIBUTES


MAP = {
    "identifier":  'urn:oasis:names:tc:SAML:2.0:attrname-format:basic',
    "fro": {k: k for k in ATTRS},
    "to": {k: k for k in ATTRS}
}
