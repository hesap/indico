# -*- coding: utf-8 -*-
##
##
## This file is part of Indico.
## Copyright (C) 2002 - 2014 European Organization for Nuclear Research (CERN).
##
## Indico is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or (at your option) any later version.
##
## Indico is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with Indico. If not, see <http://www.gnu.org/licenses/>.

import MaKaC.webinterface.rh.xmlGateway as mod_rh_xmlGateway

from indico.web.flask.wrappers import IndicoBlueprint


legacy = IndicoBlueprint('legacy', __name__)


# Routes for xmlGateway.py
legacy.add_url_rule('/xmlGateway.py',
                    'xmlGateway',
                    mod_rh_xmlGateway.RHLoginStatus,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/getCategoryInfo',
                    'xmlGateway-getCategoryInfo',
                    mod_rh_xmlGateway.RHCategInfo,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/getStatsIndico',
                    'xmlGateway-getStatsIndico',
                    mod_rh_xmlGateway.RHStatsIndico,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/loginStatus',
                    'xmlGateway-loginStatus',
                    mod_rh_xmlGateway.RHLoginStatus,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/signIn',
                    'xmlGateway-signIn',
                    mod_rh_xmlGateway.RHSignIn,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/signOut',
                    'xmlGateway-signOut',
                    mod_rh_xmlGateway.RHSignOut,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/webcastForthcomingEvents',
                    'xmlGateway-webcastForthcomingEvents',
                    mod_rh_xmlGateway.RHWebcastForthcomingEvents,
                    methods=('GET', 'POST'))

legacy.add_url_rule('/xmlGateway.py/webcastOnAir',
                    'xmlGateway-webcastOnAir',
                    mod_rh_xmlGateway.RHWebcastOnAir,
                    methods=('GET', 'POST'))


# Legacy endpoints defined in htdocs/*.py files (which need compatibility routes)
# Note: When removing/renaming endpoints, feel free to remove them in here, too, but
# it's not absolutely necessary - if there's no non-legacy endpoint with that name
# the entry in here simply does nothing.
legacy_endpoints = {
    'about', 'abstractDisplay', 'abstractDisplay-getAttachedFile', 'abstractDisplay-pdf', 'abstractManagment',
    'abstractManagment-abstractToPDF', 'abstractManagment-accept', 'abstractManagment-acceptMultiple',
    'abstractManagment-backToSubmitted', 'abstractManagment-changeTrack', 'abstractManagment-comments',
    'abstractManagment-directAccess', 'abstractManagment-editComment', 'abstractManagment-editData',
    'abstractManagment-markAsDup', 'abstractManagment-mergeInto', 'abstractManagment-newComment',
    'abstractManagment-notifLog', 'abstractManagment-orderByRating', 'abstractManagment-propToAcc',
    'abstractManagment-propToRej', 'abstractManagment-reject', 'abstractManagment-rejectMultiple',
    'abstractManagment-remComment', 'abstractManagment-trackProposal', 'abstractManagment-unMarkAsDup',
    'abstractManagment-unmerge', 'abstractManagment-withdraw', 'abstractManagment-xml', 'abstractModify',
    'abstractReviewing-notifTpl', 'abstractReviewing-notifTplCondNew', 'abstractReviewing-notifTplCondRem',
    'abstractReviewing-notifTplDisplay', 'abstractReviewing-notifTplDown', 'abstractReviewing-notifTplEdit',
    'abstractReviewing-notifTplNew', 'abstractReviewing-notifTplPreview', 'abstractReviewing-notifTplRem',
    'abstractReviewing-notifTplUp', 'abstractReviewing-reviewingSetup', 'abstractReviewing-reviewingTeam',
    'abstractsManagment', 'abstractsManagment-abstractsActions', 'abstractsManagment-mergeAbstracts',
    'abstractsManagment-newAbstract', 'abstractsManagment-participantList', 'abstractSubmission',
    'abstractSubmission-confirmation', 'abstractTools', 'abstractTools-delete', 'abstractWithdraw',
    'abstractWithdraw-recover', 'adminAnnouncement', 'adminAnnouncement-save', 'adminConferenceStyles', 'adminLayout',
    'adminLayout-addStyle', 'adminLayout-deleteStyle', 'adminLayout-saveSocial', 'adminLayout-saveTemplateSet',
    'adminLayout-setDefaultPDFOptions', 'adminLayout-styles', 'adminList',
    'adminList-switchNewsActive', 'adminMaintenance', 'adminMaintenance-pack', 'adminMaintenance-performPack',
    'adminMaintenance-performTmpCleanup', 'adminMaintenance-tmpCleanup', 'adminPlugins', 'adminPlugins-clearAllInfo',
    'adminPlugins-reload', 'adminPlugins-reloadAll', 'adminPlugins-saveOptionReloadAll',
    'adminPlugins-savePluginOptions', 'adminPlugins-savePluginTypeOptions', 'adminPlugins-toggleActive',
    'adminPlugins-toggleActivePluginType', 'adminProtection', 'adminServices-apiKeys',
    'adminServices-apiOptions', 'adminServices-apiOptionsSet', 'adminServices-ipbasedacl',
    'adminServices-ipbasedacl_fagrant', 'adminServices-ipbasedacl_farevoke', 'adminServices-oauthAuthorized',
    'adminServices-oauthConsumers', 'adminServices-webcast',
    'adminServices-webcastAddChannel', 'adminServices-webcastAddOnAir', 'adminServices-webcastAddStream',
    'adminServices-webcastAddWebcast', 'adminServices-webcastArchive', 'adminServices-webcastArchiveWebcast',
    'adminServices-webcastManualSynchronization', 'adminServices-webcastModifyChannel',
    'adminServices-webcastMoveChannelDown', 'adminServices-webcastMoveChannelUp', 'adminServices-webcastRemoveChannel',
    'adminServices-webcastRemoveFromAir', 'adminServices-webcastRemoveStream', 'adminServices-webcastRemoveWebcast',
    'adminServices-webcastSaveWebcastSynchronizationURL', 'adminServices-webcastSetup',
    'adminServices-webcastSwitchChannel', 'adminServices-webcastUnArchiveWebcast', 'adminSystem', 'adminSystem-modify',
    'adminUpcomingEvents', 'assignContributions', 'assignContributions-downloadAcceptedPapers', 'badgeTemplates',
    'badgeTemplates-badgeDesign', 'badgeTemplates-badgePrinting', 'categoryAC', 'categoryAC-setVisibility',
    'categoryConfCreationControl-setCreateConferenceControl', 'categoryConfCreationControl-setNotifyCreation',
    'categoryCreation', 'categoryCreation-create', 'categoryDataModification', 'categoryDataModification-modify',
    'categoryDataModification-tasksOption', 'categoryDisplay', 'categoryDisplay-atom', 'categoryDisplay-getIcon',
    'categoryDisplay-ical', 'categoryDisplay-rss', 'categoryFiles', 'categoryFiles-addMaterial', 'categoryMap',
    'categoryModification', 'categoryModification-actionConferences', 'categoryModification-actionSubCategs',
    'categoryStatistics', 'categoryTasks', 'categoryTasks-taskAction', 'categoryTools', 'categoryTools-delete',
    'categOverview', 'categOverview-rss', 'changeLang', 'confAbstractBook', 'confAuthorIndex', 'confDisplayEvaluation',
    'confDisplayEvaluation-display', 'confDisplayEvaluation-modif', 'confDisplayEvaluation-signIn',
    'confDisplayEvaluation-submit', 'confDisplayEvaluation-submitted', 'conferenceCFA', 'conferenceCreation',
    'conferenceCreation-createConference', 'conferenceDisplay', 'conferenceDisplay-abstractBook',
    'conferenceDisplay-abstractBookLatex', 'conferenceDisplay-accessKey', 'conferenceDisplay-getCSS',
    'conferenceDisplay-getLogo', 'conferenceDisplay-getPic', 'conferenceDisplay-ical', 'conferenceDisplay-marcxml',
    'conferenceDisplay-matPkg', 'conferenceDisplay-next', 'conferenceDisplay-performMatPkg', 'conferenceDisplay-prev',
    'conferenceDisplay-xml', 'conferenceModification', 'conferenceModification-addContribType',
    'conferenceModification-close', 'conferenceModification-closeModifKey', 'conferenceModification-data',
    'conferenceModification-dataPerform', 'conferenceModification-editContribType',
    'conferenceModification-managementAccess', 'conferenceModification-materialsAdd',
    'conferenceModification-materialsShow', 'conferenceModification-modifKey', 'conferenceModification-open',
    'conferenceModification-removeContribType',
    'conferenceModification-screenDates', 'conferenceOtherViews', 'conferenceProgram', 'conferenceProgram-pdf',
    'conferenceTimeTable', 'conferenceTimeTable-customizePdf', 'conferenceTimeTable-pdf', 'confListContribToJudge',
    'confListContribToJudge-asEditor', 'confListContribToJudge-asReviewer', 'confLogin', 'confLogin-active',
    'confLogin-disabledAccount', 'confLogin-sendActivation', 'confLogin-sendLogin', 'confLogin-unactivatedAccount',
    'confModBOA', 'confModBOA-toogleShowIds', 'confModifAC', 'confModifAC-grantModificationToAllConveners',
    'confModifAC-grantSubmissionToAllSpeakers', 'confModifAC-modifySessionCoordRights',
    'confModifAC-removeAllSubmissionRights', 'confModifAC-setVisibility', 'confModifCFA', 'confModifCFA-absFieldDown',
    'confModifCFA-absFieldUp', 'confModifCFA-abstractFields', 'confModifCFA-changeStatus',
    'confModifCFA-makeTracksMandatory', 'confModifCFA-modifyData', 'confModifCFA-performModifyData',
    'confModifCFA-preview', 'confModifCFA-removeAbstractField', 'confModifCFA-switchAttachFiles',
    'confModifCFA-switchMultipleTracks', 'confModifCFA-switchSelectSpeakerMandatory',
    'confModifCFA-switchShowAttachedFiles', 'confModifCFA-switchShowSelectSpeaker', 'confModifContribList',
    'confModifContribList-contribQuickAccess', 'confModifContribList-contribsActions',
    'confModifContribList-contribsToPDFMenu', 'confModifContribList-matPkg', 'confModifContribList-moveToSession',
    'confModifContribList-participantList', 'confModifContribList-proceedings', 'confModifDisplay',
    'confModifDisplay-addLink', 'confModifDisplay-addPage', 'confModifDisplay-addSpacer',
    'confModifDisplay-confHeader', 'confModifDisplay-custom', 'confModifDisplay-downLink',
    'confModifDisplay-formatTitleBgColor', 'confModifDisplay-formatTitleTextColor', 'confModifDisplay-menu',
    'confModifDisplay-modifyData', 'confModifDisplay-modifySystemData', 'confModifDisplay-previewCSS',
    'confModifDisplay-removeCSS', 'confModifDisplay-removeLink', 'confModifDisplay-removeLogo',
    'confModifDisplay-resources', 'confModifDisplay-saveCSS', 'confModifDisplay-saveLogo', 'confModifDisplay-savePic',
    'confModifDisplay-tickerTapeAction', 'confModifDisplay-toggleHomePage', 'confModifDisplay-toggleLinkStatus',
    'confModifDisplay-toggleNavigationBar', 'confModifDisplay-toggleSearch', 'confModifDisplay-upLink',
    'confModifDisplay-useCSS', 'confModifEpayment', 'confModifEpayment-changeStatus', 'confModifEpayment-dataModif',
    'confModifEpayment-enableSection', 'confModifEpayment-modifModule', 'confModifEpayment-performDataModif',
    'confModifEvaluation', 'confModifEvaluation-changeStatus', 'confModifEvaluation-dataModif',
    'confModifEvaluation-edit', 'confModifEvaluation-editPerformChanges', 'confModifEvaluation-performDataModif',
    'confModifEvaluation-preview', 'confModifEvaluation-results', 'confModifEvaluation-resultsOptions',
    'confModifEvaluation-resultsSubmittersActions', 'confModifEvaluation-setup', 'confModifEvaluation-specialAction',
    'confModifListings-allSpeakers', 'confModifListings-allSpeakersAction', 'confModifLog', 'confModifParticipants',
    'confModifParticipants-action', 'confModifParticipants-declinedParticipants', 'confModifParticipants-invitation',
    'confModifParticipants-pendingParticipants', 'confModifParticipants-refusal', 'confModifParticipants-setup',
    'confModifParticipants-statistics', 'confModifPendingQueues', 'confModifPendingQueues-actionConfSubmitters',
    'confModifPendingQueues-actionCoordinators', 'confModifPendingQueues-actionManagers',
    'confModifPendingQueues-actionSubmitters', 'confModifProgram', 'confModifProgram-addTrack',
    'confModifProgram-deleteTracks', 'confModifProgram-moveTrackDown', 'confModifProgram-moveTrackUp',
    'confModifProgram-performAddTrack', 'confModifRegistrants', 'confModifRegistrants-action',
    'confModifRegistrants-getAttachedFile', 'confModifRegistrants-modification',
    'confModifRegistrants-modifyAccommodation', 'confModifRegistrants-modifyMiscInfo',
    'confModifRegistrants-modifyReasonParticipation', 'confModifRegistrants-modifySessions',
    'confModifRegistrants-modifySocialEvents', 'confModifRegistrants-modifyStatuses',
    'confModifRegistrants-modifyTransaction', 'confModifRegistrants-newRegistrant',
    'confModifRegistrants-peformModifyTransaction', 'confModifRegistrants-performModifyAccommodation',
    'confModifRegistrants-performModifyMiscInfo', 'confModifRegistrants-performModifyReasonParticipation',
    'confModifRegistrants-performModifySessions', 'confModifRegistrants-performModifySocialEvents',
    'confModifRegistrants-performModifyStatuses', 'confModifRegistrants-remove', 'confModifRegistrationForm',
    'confModifRegistrationForm-actionStatuses', 'confModifRegistrationForm-changeStatus',
    'confModifRegistrationForm-dataModif', 'confModifRegistrationForm-modifStatus',
    'confModifRegistrationForm-performDataModif', 'confModifRegistrationForm-performModifStatus',
    'confModifRegistrationPreview', 'confModifReviewing-access', 'confModifReviewing-downloadTemplate',
    'confModifReviewing-paperSetup', 'confModifReviewing-setTemplate', 'confModifReviewingControl',
    'confModifSchedule', 'confModifSchedule-edit', 'confModifSchedule-reschedule', 'confModifTools',
    'confModifTools-addAlarm', 'confModifTools-allSessionsConveners', 'confModifTools-allSessionsConvenersAction',
    'confModifTools-badgeDesign', 'confModifTools-badgeGetBackground', 'confModifTools-badgePrinting',
    'confModifTools-badgePrintingPDF', 'confModifTools-badgeSaveBackground', 'confModifTools-clone',
    'confModifTools-delete', 'confModifTools-deleteAlarm', 'confModifTools-displayAlarm', 'confModifTools-matPkg',
    'confModifTools-modifyAlarm', 'confModifTools-offline', 'confModifTools-performCloning',
    'confModifTools-performMatPkg', 'confModifTools-posterDesign', 'confModifTools-posterGetBackground',
    'confModifTools-posterPrinting', 'confModifTools-posterPrintingPDF', 'confModifTools-posterSaveBackground',
    'confModifTools-saveAlarm', 'confModifTools-sendAlarmNow', 'confModifUserCompetences',
    'confRegistrantsDisplay-list', 'confRegistrationFormDisplay', 'confRegistrationFormDisplay-conditions',
    'confRegistrationFormDisplay-confirmBooking', 'confRegistrationFormDisplay-confirmBookingDone',
    'confRegistrationFormDisplay-creation', 'confRegistrationFormDisplay-creationDone',
    'confRegistrationFormDisplay-display', 'confRegistrationFormDisplay-modify',
    'confRegistrationFormDisplay-performModify', 'confRegistrationFormDisplay-signIn', 'confSpeakerIndex', 'confUser',
    'confUser-created', 'confUser-userExists', 'contact', 'contribAuthorDisplay', 'contributionAC',
    'contributionAC-setVisibility', 'contributionDisplay', 'contributionDisplay-ical', 'contributionDisplay-marcxml',
    'contributionDisplay-pdf', 'contributionDisplay-xml', 'contributionEditingJudgement', 'contributionGiveAdvice',
    'contributionListDisplay', 'contributionListDisplay-contributionsToPDF', 'contributionModification',
    'contributionModification-browseMaterial', 'contributionModification-data', 'contributionModification-materials',
    'contributionModification-materialsAdd', 'contributionModification-modifData', 'contributionModification-pdf',
    'contributionModification-setSession', 'contributionModification-setTrack', 'contributionModification-withdraw',
    'contributionModification-xml', 'contributionModifSubCont', 'contributionModifSubCont-actionSubContribs',
    'contributionModifSubCont-add', 'contributionModifSubCont-create', 'contributionReviewing',
    'contributionReviewing-assignEditing', 'contributionReviewing-assignReferee',
    'contributionReviewing-assignReviewing', 'contributionReviewing-contributionReviewingJudgements',
    'contributionReviewing-contributionReviewingMaterials', 'contributionReviewing-removeAssignEditing',
    'contributionReviewing-removeAssignReferee', 'contributionReviewing-removeAssignReviewing',
    'contributionReviewing-reviewingHistory', 'contributionTools', 'contributionTools-delete', 'domainCreation',
    'domainCreation-create', 'domainDataModification', 'domainDataModification-modify', 'domainDetails', 'domainList',
    'EMail', 'EMail-send', 'EMail-sendcontribparticipants', 'EMail-sendconvener', 'EMail-sendreg', 'errors',
    'generalInfoModification', 'generalInfoModification-update', 'getConvertedFile', 'getFile-access',
    'getFile-accessKey', 'getFile-flash', 'getFile-offlineEvent', 'getFile-wmv', 'groupDetails', 'groupList',
    'groupModification', 'groupModification-update', 'groupRegistration', 'groupRegistration-update', 'help',
    'identityCreation', 'identityCreation-changePassword', 'identityCreation-create', 'identityCreation-remove',
    'index', 'internalPage', 'JSContent-getVars', 'logOut', 'materialDisplay', 'materialDisplay-accessKey',
    'myconference', 'myconference-myContributions', 'myconference-mySessions', 'myconference-myTracks', 'news',
    'oauth-access_token', 'oauth-authorize', 'oauth-authorize_consumer', 'oauth-request_token', 'oauth-thirdPartyAuth',
    'oauth-userThirdPartyAuth', 'paperReviewingDisplay', 'paperReviewingDisplay-downloadTemplate',
    'paperReviewingDisplay-uploadPaper', 'payment', 'posterTemplates', 'posterTemplates-posterDesign',
    'posterTemplates-posterPrinting', 'resetSessionTZ', 'roomBooking', 'roomBooking-acceptBooking',
    'roomBooking-admin', 'roomBooking-adminLocation', 'roomBooking-bookingDetails',
    'roomBooking-bookingForm', 'roomBooking-bookingList', 'roomBooking-bookRoom', 'roomBooking-cancelBooking',
    'roomBooking-cancelBookingOccurrence', 'roomBooking-cloneBooking',
    'roomBooking-deleteBooking', 'roomBooking-deleteCustomAttribute', 'roomBooking-deleteEquipment',
    'roomBooking-deleteLocation', 'roomBooking-mapOfRooms', 'roomBooking-mapOfRoomsWidget',
    'roomBooking-rejectBooking', 'roomBooking-rejectBookingOccurrence',
    'roomBooking-roomDetails', 'roomBooking-roomList', 'roomBooking-roomStats',
    'roomBooking-saveBooking', 'roomBooking-saveCustomAttributes', 'roomBooking-saveEquipment',
    'roomBooking-saveLocation', 'roomBooking-search4Bookings', 'roomBooking-search4Rooms',
    'roomBooking-setDefaultLocation', 'roomBooking-statement', 'roomBookingPluginAdmin',
    'roomBookingPluginAdmin-zodbSave', 'roomMapper',
    'roomMapper-creation', 'roomMapper-details', 'roomMapper-modify', 'roomMapper-performCreation',
    'roomMapper-performModify', 'sessionDisplay', 'sessionDisplay-ical', 'sessionModifAC',
    'sessionModifAC-setVisibility', 'sessionModifComm', 'sessionModifComm-edit', 'sessionModification',
    'sessionModification-addContribs', 'sessionModification-close', 'sessionModification-contribAction',
    'sessionModification-contribList', 'sessionModification-contribQuickAccess', 'sessionModification-contribsToPDF',
    'sessionModification-editContrib', 'sessionModification-materials', 'sessionModification-materialsAdd',
    'sessionModification-modify', 'sessionModification-open', 'sessionModification-participantList',
    'sessionModifSchedule', 'sessionModifSchedule-fitSlot', 'sessionModifSchedule-slotCalc', 'sessionModifTools',
    'sessionModifTools-delete', 'signIn', 'signIn-active', 'signIn-disabledAccount', 'signIn-sendActivation',
    'signIn-sendLogin', 'signIn-sso', 'signIn-unactivatedAccount', 'subContributionDisplay',
    'subContributionDisplay-marcxml', 'subContributionModification', 'subContributionModification-data',
    'subContributionModification-materials', 'subContributionModification-materialsAdd',
    'subContributionModification-modifData', 'subContributionTools', 'subContributionTools-delete', 'taskManager',
    'trackAbstractModif', 'trackAbstractModif-abstractAction', 'trackAbstractModif-abstractToPDF',
    'trackAbstractModif-accept', 'trackAbstractModif-commentEdit', 'trackAbstractModif-commentNew',
    'trackAbstractModif-commentRem', 'trackAbstractModif-comments', 'trackAbstractModif-directAccess',
    'trackAbstractModif-markAsDup', 'trackAbstractModif-proposeForOtherTracks', 'trackAbstractModif-proposeToBeAcc',
    'trackAbstractModif-proposeToBeRej', 'trackAbstractModif-reject', 'trackAbstractModif-unMarkAsDup',
    'trackModContribList', 'trackModContribList-contribAction', 'trackModContribList-contribQuickAccess',
    'trackModContribList-contribsToPDF', 'trackModContribList-participantList', 'trackModifAbstracts',
    'trackModifCoordination', 'trackModification', 'trackModification-modify', 'trackModification-performModify',
    'updateNews', 'userAbstracts', 'userAbstracts-pdf', 'userAPI', 'userAPI-block', 'userAPI-create', 'userAPI-delete',
    'userBaskets', 'userDashboard', 'userDetails', 'userList', 'userManagement',
    'userManagement-switchAuthorisedAccountCreation', 'userManagement-switchModerateAccountCreation',
    'userManagement-switchNotifyAccountCreation', 'userMerge', 'userPreferences', 'userRegistration',
    'userRegistration-active', 'userRegistration-created', 'userRegistration-disable', 'userRegistration-UserExist',
    'wcalendar', 'wcalendar-select', 'xmlGateway', 'xmlGateway-getCategoryInfo', 'xmlGateway-getStatsIndico',
    'xmlGateway-getStatsRoomBooking', 'xmlGateway-loginStatus', 'xmlGateway-signIn', 'xmlGateway-signOut',
    'xmlGateway-webcastForthcomingEvents', 'xmlGateway-webcastOnAir'
}
